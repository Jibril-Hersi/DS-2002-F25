import os, sys, json, glob
import pandas as pd

def _load_lookup_data(lookup_dir: str) -> pd.DataFrame:
    """Read all JSON card files and flatten to a lookup table."""
    all_lookup_df = []
    for path in glob.glob(os.path.join(lookup_dir, "*.json")):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        rows = data.get("data", [])
        if not rows:
            continue
        df = pd.json_normalize(rows)

        # Market price: prefer holofoil, fallback to normal, else 0.0
        df["card_market_value"] = (
            df.get("tcgplayer.prices.holofoil.market")
              .fillna(df.get("tcgplayer.prices.normal.market"))
              .fillna(0.0)
              .astype(float)
        )

        df = df.rename(columns={
            "id": "card_id",
            "name": "card_name",
            "number": "card_number",
            "set.id": "set_id",
            "set.name": "set_name",
        })

        keep = ["card_id","card_name","card_number","set_id","set_name","card_market_value"]
        df = df[[c for c in keep if c in df.columns]].copy()
        all_lookup_df.append(df)

    if not all_lookup_df:
        return pd.DataFrame(columns=["card_id","card_name","card_number","set_id","set_name","card_market_value"])

    lookup_df = pd.concat(all_lookup_df, ignore_index=True)
    lookup_df = (
        lookup_df.sort_values("card_market_value", ascending=False)
                 .drop_duplicates(subset=["card_id"], keep="first")
                 .reset_index(drop=True)
    )
    return lookup_df


def _load_inventory_data(inventory_dir: str) -> pd.DataFrame:
    """Read all CSVs and create a unified card_id (set_id-number)."""
    frames = []
    for path in glob.glob(os.path.join(inventory_dir, "*.csv")):
        frames.append(pd.read_csv(path))
    if not frames:
        return pd.DataFrame(columns=[
            "card_name","set_id","card_number","binder_name","page_number","slot_number","card_id"
        ])
    inventory_df = pd.concat(frames, ignore_index=True)
    inventory_df["set_id"] = inventory_df["set_id"].astype(str)
    inventory_df["card_number"] = inventory_df["card_number"].astype(str)
    inventory_df["card_id"] = inventory_df["set_id"] + "-" + inventory_df["card_number"]
    return inventory_df


def _coalesce(df: pd.DataFrame, out_col: str, prefer: str, fallback: str) -> None:
    """Create out_col by preferring one column and falling back to another."""
    if prefer in df.columns and fallback in df.columns:
        df[out_col] = df[prefer].where(df[prefer].notna(), df[fallback])
    elif prefer in df.columns:
        df[out_col] = df[prefer]
    elif fallback in df.columns:
        df[out_col] = df[fallback]
    else:
        df[out_col] = pd.NA


def update_portfolio(inventory_dir: str, lookup_dir: str, output_file: str) -> None:
    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)

    if inventory_df.empty:
        print("ERROR: No inventory CSVs found or inventory is empty.", file=sys.stderr)
        cols = ["index","binder_name","page_number","slot_number",
                "card_id","card_name","set_name","card_number","card_market_value"]
        pd.DataFrame(columns=cols).to_csv(output_file, index=False)
        return

    keep_lookup = ["card_id","card_name","set_name","card_number","card_market_value"]
    lookup_slim = lookup_df[keep_lookup] if not lookup_df.empty else pd.DataFrame(columns=keep_lookup)

    # Merge inventory with lookup (use suffixes so we can coalesce)
    merged = pd.merge(inventory_df, lookup_slim, on="card_id", how="left", suffixes=("_inv","_look"))

    # ensure we have name/number even if both sources are missing
    if "card_name" not in merged.columns:
        merged["card_name"] = merged.get("card_name_look", merged.get("card_name_inv", ""))
    if "card_number" not in merged.columns:
        merged["card_number"] = merged.get("card_number_look", merged.get("card_number_inv", ""))

    # Coalesce name/number to single columns (prefer lookup, fallback inventory)
    _coalesce(merged, "card_name", "card_name_look", "card_name_inv")
    _coalesce(merged, "card_number", "card_number_look", "card_number_inv")

    merged["card_market_value"] = merged.get("card_market_value", pd.Series([0]*len(merged))).fillna(0.0)
    merged["set_name"] = merged.get("set_name", pd.Series(["NOT_FOUND"]*len(merged))).fillna("NOT_FOUND")

    merged["index"] = (
        merged["binder_name"].astype(str) + ":" +
        merged["page_number"].astype(str) + ":" +
        merged["slot_number"].astype(str)
    )

    final_cols = ["index","binder_name","page_number","slot_number",
                  "card_id","card_name","set_name","card_number","card_market_value"]
    for c in final_cols:
        if c not in merged.columns:
            merged[c] = "" if c != "card_market_value" else 0.0

    merged[final_cols].to_csv(output_file, index=False)
    print(f"Wrote portfolio: {output_file}")


def main():
    update_portfolio("./card_inventory", "./card_set_lookup", "card_portfolio.csv")


def test():
    update_portfolio("./card_inventory_test", "./card_set_lookup_test", "test_card_portfolio.csv")


if __name__ == "__main__":
    print("Starting update_portfolio.py in TEST mode ...", file=sys.stderr)
    test()
