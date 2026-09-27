import csv
from html.parser import HTMLParser


class DetailedXPathParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []  # Tracks tag hierarchy
        self.tag_counts = []  # Tracks sibling counts at each level
        self.records = []
        self.current_text = ""
        self.current_tag_info = None

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)

        # Calculate sibling index for duplicate tags
        if self.tag_counts:
            parent_counts = self.tag_counts[-1]
            parent_counts[tag] = parent_counts.get(tag, 0) + 1
            index = parent_counts[tag]
        else:
            index = 1

        self.stack.append((tag, index, attr_dict))
        self.tag_counts.append({})
        self.current_text = ""

        # Build absolute XPath
        abs_xpath_parts = [f"{t}[{i}]" for t, i, _ in self.stack]
        abs_xpath = "/" + "/".join(abs_xpath_parts)

        # Build Relative Attribute-based XPath
        rel_xpath = f"//{tag}"
        if 'id' in attr_dict:
            rel_xpath = f"//{tag}[@id='{attr_dict['id']}']"
        elif 'name' in attr_dict:
            rel_xpath = f"//{tag}[@name='{attr_dict['name']}']"
        elif 'class' in attr_dict:
            rel_xpath = f"//{tag}[@class='{attr_dict['class']}']"
        elif 'onclick' in attr_dict:
            rel_xpath = f"//{tag}[@onclick='{attr_dict['onclick']}']"

        # Build detailed name identifier
        id_str = f"id='{attr_dict['id']}' " if 'id' in attr_dict else ""
        class_str = f"class='{attr_dict['class']}' " if 'class' in attr_dict else ""
        name_str = f"name='{attr_dict['name']}' " if 'name' in attr_dict else ""

        identifier = f"<{tag} {id_str}{name_str}{class_str}>".strip()

        # Build attributes summary
        attributes_summary = ", ".join([f"{k}='{v}'" for k, v in attr_dict.items()])

        self.current_tag_info = {
            "tag": tag,
            "identifier": identifier,
            "attributes": attributes_summary if attributes_summary else "N/A",
            "abs_xpath": abs_xpath,
            "rel_xpath": rel_xpath
        }

    def handle_data(self, data):
        cleaned_data = data.strip()
        if cleaned_data:
            self.current_text += cleaned_data + " "

    def handle_endtag(self, tag):
        if self.current_tag_info and self.stack and self.stack[-1][0] == tag:
            text = self.current_text.strip()
            if text:
                # Append text info to identifier if present
                self.current_tag_info["identifier"] += f" (Text: '{text}')"

            self.records.append([
                self.current_tag_info["tag"],
                self.current_tag_info["identifier"],
                self.current_tag_info["attributes"],
                self.current_tag_info["abs_xpath"],
                self.current_tag_info["rel_xpath"]
            ])
            self.current_tag_info = None

        if self.stack:
            self.stack.pop()
            self.tag_counts.pop()


def extract_detailed_xpaths(html_file_path, output_csv="xpaths_detailed.csv"):
    parser = DetailedXPathParser()

    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    parser.feed(html_content)

    headers = [
        "Tag Type",
        "ID / Name / Class Identifier",
        "Attributes / Actions",
        "Absolute XPath",
        "Relative XPath (Attributes)"
    ]

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(parser.records)

    print(f"Successfully processed '{html_file_path}' -> Saved {len(parser.records)} XPaths to '{output_csv}'")


# --- Run the parser ---
if __name__ == "__main__":
    # Ensure 'page.html' is in the same directory as this script
    extract_detailed_xpaths("a.html", "xpaths_detailed.csv")