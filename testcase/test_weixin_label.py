from api.labelmanagement import LabelManagement
class TestWeixinLsbel:
    def test_create_label(self):
       assert "created" in LabelManagement().create_label('UI', '12')['errmsg']
    def test_update_label(self):
       assert "updated" in LabelManagement().update_label('UI design', '12')['errmsg']
    def test_get_label(self):
       assert "UI design" in LabelManagement().get_label('12')['tagname']
    def test_delete_label(self):
       assert "deleted" in LabelManagement().delete_label('12')['errmsg']