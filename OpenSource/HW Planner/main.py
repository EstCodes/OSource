class HomeworkPlanner:
    def __init__(self, id, title, subject, due_datetime , priority , status, list_subjects):
        self.id = id
        self.title = title
        self.subject = subject
        self.due_datetime = due_datetime
        self.priority = priority
        self.status = status
        self.list_subjects = list_subjects

    def add_title(self):
        self.title = input("Enter a title: ")

# Create a subject
    def create_subject(self):
        self.subject = input("Enter a subject: ")

        self.list_subjects.append(self.subject)
        print("Subject successfully added!")

# Select a subject
    def subject_selector(self, subjectSelecter=None):
        print("""
==============================================
              Subject selecter.
              1) Add
              2) Create
==============================================
""")
        subjectSelecter = int(input("Select a number"))

        if subjectSelecter not in [1, 2]:
            print("Something is wrong. Enter 1 or 2.")
            # Add a Loop instead of recursion
        elif subjectSelecter == 2:
            self.create_subject()
        else:
            print("Lets add a Subject created.")

            if not self.list_subjects:
                print("There are no subjects in here. Lets create some.")
                self.create_subject()
            else:
                for subject in self.list_subjects:
                    print(subject)

if __name__ == "__main__":
    # Create an instance of HomeworkPlanner with sample data
    planner = HomeworkPlanner(
        id=1,
        title="Sample Homework",
        subject="Math",
        due_datetime="2023-12-01 10:00",
        priority="High",
        status="Pending",
        list_subjects=[]
    )
    
    # Try the subject selector
    planner.subject_selector()