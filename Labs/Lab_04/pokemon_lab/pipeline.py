
import sys
import update_portfolio, generate_summary

def run_production_pipeline() -> None:
    print("[pipeline] Starting production run ...", file=sys.stderr)
    print("[pipeline] Step 1: Update portfolio (ETL) ...", file=sys.stderr)
    update_portfolio.main()
    print("[pipeline] Step 2: Generate summary (report) ...", file=sys.stderr)
    generate_summary.main()
    print("[pipeline] Done.", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()
