import pyexcel

a_list = [
{
    "Name": 'Adam',
    "Age": 28
},
{
    "Name": 'Beatrice',
    "Age": 29
},
{
    "Name": 'Ceri',
    "Age": 30
},
{
    "Name": 'Dean',
    "Age": 26
}
]

pyexcel.save_as(records=a_list, dest_file_name="myfile.xlsx")