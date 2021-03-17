TEST_CONFIG = [
    {
        "table_name": "SUPPLIER",
        "columns": [
            {
                "column_type": "int",
                "name": "s_suppkey"
            },
            {
                "column_type": "string",
                "name": "s_name"
            },
            {
                "column_type": "string",
                "name": "s_address"
            },
            {
                "column_type": "string",
                "name": "s_nationkey"
            },
            {
                "column_type": "string",
                "name": "s_phone"
            },
            {
                "column_type": "decimal",
                "name": "s_acctbal"
            },
            {
                "column_type": "string",
                "name": "s_comment"
            }
        ]
    },
    {
        "table_name": "CUSTOMER",
        "columns": [
            {
                "column_type": "int",
                "name": "c_custkey"
            },
            {
                "column_type": "string",
                "name": "c_name"
            },
            {
                "column_type": "string",
                "name": "c_address"
            },
            {
                "column_type": "string",
                "name": "c_nationkey"
            },
            {
                "column_type": "string",
                "name": "c_phone"
            },
            {
                "column_type": "decimal",
                "name": "c_acctbal"
            },
            {
                "column_type": "string",
                "name": "c_mktsegment"
            },
            {
                "column_type": "string",
                "name": "c_comment"
            }
        ]
    },
    {
        "table_name": "LINEITEM",
        "columns": [
            {
                "column_type": "int",
                "name": "l_orderkey"
            },
            {
                "column_type": "int",
                "name": "l_partkey"
            },
            {
                "column_type": "int",
                "name": "l_suppkey"
            },
            {
                "column_type": "int",
                "name": "l_linenumber"
            },
            {
                "column_type": "decimal",
                "name": "l_quantity"
            },
            {
                "column_type": "decimal",
                "name": "l_extendedprice"
            },
            {
                "column_type": "decimal",
                "name": "l_discount"
            },
            {
                "column_type": "decimal",
                "name": "l_tax"
            },
            {
                "column_type": "string",
                "name": "l_returnflag"
            },
            {
                "column_type": "string",
                "name": "l_linestatus"
            },
            {
                "column_type": "date",
                "name": "l_shipdate"
            },
            {
                "column_type": "date",
                "name": "l_commitdate"
            },
            {
                "column_type": "date",
                "name": "l_receiptdate"
            },
            {
                "column_type": "string",
                "name": "l_shippinstruct"
            },
            {
                "column_type": "string",
                "name": "l_shipmode"
            },
            {
                "column_type": "string",
                "name": "l_comment"
            }
        ]
    },
    {
        "table_name": "ORDERS",
        "columns": [
            {
                "column_type": "int",
                "name": "o_orderkey"
            },
            {
                "column_type": "int",
                "name": "o_custkey"
            },
            {
                "column_type": "string",
                "name": "o_orderstatus"
            },
            {
                "column_type": "string",
                "name": "o_totalprice"
            },
            {
                "column_type": "date",
                "name": "o_orderdate"
            },
            {
                "column_type": "string",
                "name": "o_orderpriority"
            },
            {
                "column_type": "string",
                "name": "o_clerk"
            },
            {
                "column_type": "int",
                "name": "o_shippriority"
            },
            {
                "column_type": "string",
                "name": "o_comment"
            }
        ]
    },
    {
        "table_name": "REGION",
        "columns": [
            {
                "column_type": "int",
                "name": "r_regionkey"
            },
            {
                "column_type": "string",
                "name": "r_name"
            },
            {
                "column_type": "string",
                "name": "r_comment"
            }
        ]
    },
    {
        "table_name": "nation",
        "columns": [
            {
                "column_type": "int",
                "name": "n_nationkey"
            },
            {
                "column_type": "string",
                "name": "n_name"
            },
            {
                "column_type": "string",
                "name": "n_regionkey"
            },
            {
                "column_type": "string",
                "name": "n_comment"
            }
        ]
    }
]
