import csv
from gui import Gui


class Logic(Gui):
    """
    A class that handles the logic for voting system interactions.

    Class Attributes:
        __BIANCA (int): Constant representing Bianca as a candidate.
        __EDWARD (int): Constant representing Edward as a candidate.
        __FELICIA (int): Constant representing Felicia as a candidate.
        __VOTER_LOG (str): Filename for the voter log CSV file.
    """

    __BIANCA: int = 1
    __EDWARD: int = 2
    __FELICIA: int = 3
    __VOTER_LOG: str = "voterlog.csv"

    def vote(self) -> None:
        """
        Process a voter's vote.

        Performs these actions:
        1. Validates user ID input
        2. Checks candidate selection
        3. Verifies if the voter is a new voter
        4. Logs the vote in the voter log file
        5. Updates GUI with success or error message

        Raises:
            ValueError: If ID is empty or no candidate is selected
            ValueError: If the voter has already voted
        """
        user_id: str = self.input_id.get().strip()
        user_vote: int = self.radio_choice.get()

        try:
            if user_id is None or user_id == "":
                raise ValueError("ID is required. Please enter ID.")
            if user_vote == 0:
                raise ValueError(
                    "Candidate selection is required.\nPlease choose a candidate."
                )
            if self.__is_new_voter(user_id, Logic.__VOTER_LOG):
                with open(Logic.__VOTER_LOG, "a+", newline="") as voter_file:
                    csv_writer = csv.writer(voter_file)
                    if user_vote == Logic.__BIANCA:
                        csv_writer.writerow([user_id, "Bianca"])
                    if user_vote == Logic.__EDWARD:
                        csv_writer.writerow([user_id, "Edward"])
                    if user_vote == Logic.__FELICIA:
                        csv_writer.writerow([user_id, "Felicia"])
                    self.label_alert.config(
                        text="Vote registered successfully!", fg="green"
                    )
                    self.label_alert.pack(padx=5)
            else:
                raise ValueError("This ID has already voted.")

        except ValueError as ve:
            self.label_alert.config(text=str(ve), fg="red")
            self.label_alert.pack(padx=5)

    def __is_new_voter(self, id: str, csv_file_name: str) -> bool:
        """
        Verify if a voter is a new voter.

        Performs these actions:
        1. Opens the voter log file
        2. Checks if the given ID exists in the log
        3. Returns boolean indicating voter's status

        Args:
            id (str): The voter's unique identifier
            csv_file_name (str): Path to the voter log CSV file

        Returns:
            bool: True if the voter is new (has not voted before), False otherwise

        - Returns True if the voter log file does not exist
        - Returns True if no matching ID is found
        - Returns False if a matching ID is found
        """
        try:
            with open(csv_file_name, "r", newline="") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line and line[0] == id:
                        return False
            return True
        except FileNotFoundError:
            return True
        except Exception:
            return True