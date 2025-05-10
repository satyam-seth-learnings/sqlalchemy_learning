from models import create_table
from services import (
    create_user,
    get_single_user,
    get_all_user,
    update_user_email,
    delete_user,
)

# Create Table
create_table()

# # Insert Data
# create_user("sonam", "sonam@example.com")
# create_user("raj", "raj@example.com")

# # # Fetch Data
# # print(get_single_user(1))
# print(get_all_user())

# # Update Data
# update_user_email(1, "sonam@newdomain.com")

# # Delete Data
# delete_user(2)
