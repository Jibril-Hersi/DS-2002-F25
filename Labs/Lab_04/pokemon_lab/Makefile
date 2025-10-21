
PORTFOLIO_CSV := card_portfolio.csv
TEST_PORTFOLIO_CSV := test_card_portfolio.csv

.PHONY: all Add_Set Refresh_Sets Portfolio_Build Clean Test
all: Portfolio_Build

Add_Set:
	@echo "--- Adding New Card Set ---"
	@./add_card_set.sh

Refresh_Sets:
	@echo "--- Refreshing All Card Sets ---"
	@./refresh_card_sets.sh

Portfolio_Build: update_portfolio.py generate_summary.py pipeline.py
	@echo "--- Starting Portfolio Build Workflow ---"
	@echo "Do you want to add a NEW card set? (yes/no)"
	@read USER_ADD; \
	if [ "$$USER_ADD" = "yes" ]; then \
		$(MAKE) Add_Set; \
		echo "Card set added. Add another? (yes/no)"; \
		read USER_ADD_AGAIN; \
		if [ "$$USER_ADD_AGAIN" = "yes" ]; then \
			$(MAKE) Add_Set; \
		fi; \
	fi
	@echo "Do you want to refresh ALL existing card sets? (yes/no)"
	@read USER_REFRESH; \
	if [ "$$USER_REFRESH" = "yes" ]; then \
		$(MAKE) Refresh_Sets; \
	fi
	@python ./pipeline.py

Test: update_portfolio.py generate_summary.py card_set_lookup_test/*.json
	@echo "--- Running Test Pipeline (Built-in Test Modes) ---"
	@python ./update_portfolio.py
	@python ./generate_summary.py
	@echo "Test complete."

Clean:
	@echo "--- Cleaning Generated Files ---"
	@rm -f $(PORTFOLIO_CSV) $(TEST_PORTFOLIO_CSV)
	@rm -f card_set_lookup/*.json
	@echo "Clean complete."
