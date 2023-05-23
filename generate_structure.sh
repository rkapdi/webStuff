#!/bin/bash

# Create the project folder
mkdir -p "Project Folder/Proposal"
mkdir -p "Project Folder/Website Files/css"
mkdir -p "Project Folder/Website Files/js"
mkdir -p "Project Folder/Website Files/images"
mkdir -p "Project Folder/Website Files/pages"
mkdir -p "Project Folder/Documentation"
mkdir -p "Project Folder/Media/Photos"
mkdir -p "Project Folder/Media/Videos"

# Create the files
touch "Project Folder/Proposal/Project Proposal Document.pdf"
touch "Project Folder/Website Files/index.html"
touch "Project Folder/Website Files/css/styles.css"
touch "Project Folder/Website Files/js/script.js"
touch "Project Folder/Website Files/images/logo.png"
touch "Project Folder/Website Files/images/banner.jpg"
touch "Project Folder/Website Files/pages/flight-search.html"
touch "Project Folder/Website Files/pages/booking.html"
touch "Project Folder/Website Files/pages/account.html"
touch "Project Folder/Website Files/pages/discounts.html"
touch "Project Folder/Website Files/pages/flight-info.html"
touch "Project Folder/Website Files/cross-reference.html"
touch "Project Folder/Website Files/evaluation-form.html"
touch "Project Folder/Documentation/Front Page.pdf"
touch "Project Folder/Documentation/Business Statement.pdf"
touch "Project Folder/Documentation/Objectives.pdf"
touch "Project Folder/Documentation/Project Description.pdf"

# Create placeholder files in Media folder
for i in {1..10}; do
    touch "Project Folder/Media/Photos/image${i}.jpg"
done

for i in {1..5}; do
    touch "Project Folder/Media/Videos/video${i}.mp4"
done

echo "File structure created successfully!"

