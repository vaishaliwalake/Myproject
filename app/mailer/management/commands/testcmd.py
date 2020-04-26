#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import random
from uuid import uuid4

from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from django.utils.text import slugify
from django.utils.timezone import now

#from app.mailer.models import Company

company_suffixes = [
    "Company", "Investors", "Dupers",
    "Outdoors", "Computers", "Velvet", "Corporation",
    "Industries"
]

company_post_suffixes = [
    "Inc", "Ltd", "Corp.", "GmbH", "Oy", "Ab"
]

fruits = [
    "Apple",
    "Apricot",
    "Avocado",
    "Banana",
    "Bilberry",
    "Blackberry",
    "Blackcurrant",
    "Blood Orange",
    "Blueberry",
    "Boysenberry",
    "Breadfruit",
    "Cantaloupe",
    "Cherimoya",
    "Cherry",
    "Chili",
    "Clementine",
    "Cloudberry",
    "Coconut",
    "Cranberry",
    "Cucumber",
    "Currant",
    "Damson",
    "Date",
    "Dragonfruit",
    "Durian",
    "Eggplant",
    "Elderberry",
    "Feijoa",
    "Fig",
    "Goji",
    "Gooseberry",
    "Grape",
    "Grapefruit",
    "Guava",
    "Honeydew",
    "Huckleberry",
    "Jackfruit",
    "Jambul",
    "Jujube",
    "Kiwi fruit",
    "Kumquat",
    "Lemon",
    "Lime",
    "Loquat",
    "Lychee",
    "Mandarine",
    "Mango",
    "Mangosteen",
    "Melon",
    "Mulberry",
    "Nectarine",
    "Nut",
    "Olive",
    "Orange",
    "Pamelo",
    "Papaya",
    "Passionfruit",
    "Peach",
    "Pear",
    "Pepper",
    "Persimmon",
    "Physalis",
    "Pineapple",
    "Plum",
    "Pomegranate",
    "Pomelo",
    "Quince",
    "Rambutan",
    "Raspberry",
    "Redcurrant",
    "Satsuma",
    "Strawberry",
    "Tamarillo",
    "Tangerine",
    "Watermelon",
]

firstnames = [
    "Alexander",
    "Arthur",
    "Benjamin",
    "Bernardo",
    "Carter",
    "Davi",
    "Dylan",
    "Ethan",
    "Gabriel",
    "Guilherme",
    "Ian",
    "Jack",
    "Jacob",
    "Joaquín",
    "Juan",
    "Lautaro",
    "Liam",
    "Logan",
    "Lucas",
    "Benjamin",
    "Mason",
    "Mateo Daniel",
    "Matheus",
    "Miguel",
    "Nathan",
    "Noah",
    "Owen",
    "Pedro",
    "Rafael",
    "Samuel",
    "Santiago",
    "Santino",
    "Thiago",
    "William"
]
lastnames = [
    "Thompson",
    "White",
    "Hughes",
    "Edwards",
    "Green",
    "Hall",
    "Wood",
    "Harris",
    "Lewis",
    "Martin",
    "Jackson",
    "Clarke",
    "Clark",
    "Turner",
    "Hill",
    "Scott",
    "Cooper",
    "Morris",
    "Ward",
    "Moore",
    "King",
    "Watson",
    "Baker",
    "Harrison",
    "Morgan",
    "Patel",
    "Young",
    "Allen"
]


def generate_company_name():
    name = "%s %s" % (random.choice(fruits), random.choice(company_suffixes))
    if random.randint(0, 1000) < 500:
        name += " %s" % random.choice(company_post_suffixes)
    return name


class Command(BaseCommand):

    @atomic
    def handle(self, *args, **options):
        companies = 500
        contacts = 10
        orders = 10

        for idx in range(0, companies):
            print(idx)
