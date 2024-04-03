import config
import gpt


content = (
    config.PROMPT_EXECUTIVE_SUMMARY["role"]
    + " "
    + config.PROMPT_EXECUTIVE_SUMMARY["restrictions"]
    + " "
    + config.PROMPT_EXECUTIVE_SUMMARY["examples"]
)


question = """Struggling regional lender New York Community Bancorp
 announced a $1 billion capital raise and a leadership shake-up on Wednesday, headlined by former Treasury Secretary Steven Mnuchin, leading to a sharp rebound for its stock.

NYCB has agreed to a deal with several investment firms including Mnuchin’s Liberty Strategic Capital, Hudson Bay Capital and Reverence Capital Partners for more than $1 billion in exchange for equity in the regional bank, according to a press release Wednesday afternoon.

Mnuchin will be one of four new members of the bank’s board of directors as part of the deal. Joseph Otting, former comptroller of the currency, is also joining the board and taking over as CEO.

The stock jumped sharply after the announcement, but trading was highly volatile. Shares were briefly halted, up nearly 30% for the day. They gave back some of those gains when trading resumed and finished the day up more than 7% after several more halts.

Prior to the press release, the stock was down 42%, amid reports from Reuters and The Wall Street Journal that NYCB was exploring a capital raise."
"""


response = gpt.main(
    question=config.PROMPT_EXECUTIVE_SUMMARY["examples"],
    content=content,
)

print(response)
