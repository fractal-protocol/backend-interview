# Portfolio Value Tracker - Interview Coding Exercise

## Objective
Build a system to track the total USD value of assets in one or more cryptocurrency wallets on a specified blockchain network. The system should periodically fetch asset balances, retrieve prices, calculate total value, and log results.

## Advice
Read the prompt carefully and ask clarifying questions to understand requirements. Use provided documentation and resources to guide your work. If unfamiliar with blockchain concepts, focus on coding, problem-solving, and explaining your approach. **Disable AI / LLM assistance during the interview.**

## Initial Task
Implement a tracker for a single wallet address to monitor specified assets (details provided during the interview):
- **Native Token**: The blockchain's native cryptocurrency (e.g., ETH).
- **ERC20 Token**: A standard token contract (address provided).
- **ERC4626 Vault**: A vault contract holding an underlying token (address provided).

### Requirements:
1. **Fetch Balances**: Use Web3 library to query balance.
2. **Fetch Prices**: Use a provided price [API](https://prices.augustdigital.io/docs) to get token prices.
3. **Calculate Total Value**: Sum the USD value of all assets, accounting for token decimals.
4. **Logging**: Log the total portfolio value every 5 seconds with a timestamp. Store the last 10 values in a simple data structure (e.g., list).
5. **Error Handling**: Handle API or blockchain query failures.
6. **Verification**: Compare results with a provided portfolio overview ([e.g.](https://debank.com/profile/0x9B974aF13ae64775E7E96fd92d9089b479cB57C5)).

## Follow-Up Tasks
Discuss and implement (time permitting) the following extensions. Explain your design choices, trade-offs, and assumptions in comments or verbally.

### 1. Dynamic Asset Tracking
- Support a configurable list of assets via a JSON file.
- Replace the simple history storage with an efficient data structure (ideally O(1) operations).
- Add a feature: Log a moving average of recent values (e.g., 5-point average).
- Discuss: Why your chosen data structure? Time / space complexity? Alternatives?

### 2. Multi-Wallet Support & Optimization
- Track multiple wallets (list provided in configuration).
- Implement caching for prices.
- Prioritize wallet updates.
- Discuss: Caching benefits VS drawbacks? How to handle concurrency?

### 3. Modular Design & Scalability
- Refactor code into modular components.
- Add a simple analytical feature.
- Discuss: How would you scale to 1.000+ wallets? How about 1.000.000+ wallets? Bottlenecks? Optimization strategies (e.g., batch queries)?

## Technical Notes
- **Blockchain Library**: Use Web3.py.
- **Price API**: Use the provided API endpoint.
- **Block Explorer**: Use the provided explorer for contract details.
- **Files**:
  - `main.py`: Write your implementation here.
  - `ierc20_abi.json` & `ierc4626_abi.json`: Contract ABIs.
  - `configuration.json`: Configuration for assets / wallets (create for follow-ups).
  - `requirements.txt`: Dependencies (add if needed).
- Run in a loop with 5-second intervals.

## TL;DR
1. Clone repository, install dependencies.
2. Implement core task in `main.py`.
3. Verify results using provided portfolio link.
4. Discuss / implement follow-ups as time allows.

Good luck! Feel free to ask questions during the interview.
