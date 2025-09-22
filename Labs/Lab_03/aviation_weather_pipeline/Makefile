.PHONY: all fetch analyze clean

analyze: fetch
	@echo "==> Starting analyze step..."
	@./analyze_data.sh
	@echo "==> Analyze complete. Output: weather_report.csv"
	@echo "==> Pipeline completed successfully."

fetch:
	@echo "==> Starting fetch step..."
	@./fetch_metars.sh
	@echo "==> Fetch complete. Raw data in: raw_metars/"

clean:
	@echo "==> Cleaning generated files..."
	@rm -rf raw_metars weather_report.csv
	@echo "==> Clean complete."

all: analyze
