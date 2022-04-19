from .extension import ma

class CustomersSchema(ma.Schema):
    class Meta:
        fields = ("customerid","customer_name", "contact_name", "address", "city", "postalcode", "country")