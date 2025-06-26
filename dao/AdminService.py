from util.DBConnUtil import get_connection
from dao.IAdminService import IAdminService
from entity.Admin import Admin

class AdminService(IAdminService):

    def __init__(self, config):
        self.config = config

    def get_admin_by_id(self, admin_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE AdminID = %s", (admin_id,))
        row = cursor.fetchone()
        conn.close()
        return Admin(*row) if row else None

    def get_admin_by_username(self, username):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE Username = %s", (username,))
        row = cursor.fetchone()
        conn.close()
        return Admin(*row) if row else None

    def register_admin(self, admin):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Admin (AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (admin.admin_id, admin.first_name, admin.last_name, admin.email, admin.phone_number,
              admin.username, admin.password, admin.role, admin.join_date))
        conn.commit()
        conn.close()

    def update_admin(self, admin):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Admin SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s,
            Username=%s, Password=%s, Role=%s, JoinDate=%s WHERE AdminID=%s
        """, (admin.first_name, admin.last_name, admin.email, admin.phone_number,
              admin.username, admin.password, admin.role, admin.join_date, admin.admin_id))
        conn.commit()
        conn.close()

    def delete_admin(self, admin_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Admin WHERE AdminID = %s", (admin_id,))
        conn.commit()
        conn.close()
