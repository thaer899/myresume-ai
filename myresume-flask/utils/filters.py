
def filter_data_with_keywords(data, keywords):
    try:
        print('########### Starting data filtration with keywords:', keywords)
        print('########### Data to be filtered:', data)
        all_keywords = [k['word'] for k in keywords] + \
            [syn for k in keywords for syn in k['synonyms']]

        def contains_keyword(text, keywords):
            if not isinstance(text, str):
                text = str(text)
            return any(keyword.lower() in text.lower()
                       for keyword in keywords)

        def filter_items(items, keywords):
            return [
                item for item in items if any(
                    contains_keyword(value, keywords)
                    for value in item.values()
                )
            ]

        def filter_string_list(items, keywords):
            return [item for item in items if contains_keyword(item, keywords)]

        filtered_data = {}

        # Iterating through each section in data
        for section in data.keys():
            # If section key matches a keyword, take all data without filtering
            if contains_keyword(section, all_keywords):
                filtered_data[section] = data[section]
                print(
                    f"All {section} Data taken for key match:", data[section])
            else:
                # Old logic for each section type if the section key doesn’t
                # match the keywords
                if section in ['education', 'employment', 'languages',
                               'personal', 'references']:
                    filtered_data[section] = filter_items(
                        data[section], all_keywords)
                    print(f'Filtered {section.capitalize()} Data:',
                          filtered_data[section])
                elif section == 'interests':
                    filtered_data[section] = filter_string_list(
                        data[section], all_keywords)
                    print(f'Filtered {section.capitalize()} Data:',
                          filtered_data[section])
                elif section == 'resume':
                    filtered_data[section] = {key: value
                                              for key, value in data[section]
                                              .items(
                                              ) if contains_keyword(
                                                  str(value), all_keywords)}
                    print(f'Filtered {section.capitalize()} Data:',
                          filtered_data[section])
                elif section == 'skills':
                    filtered_data[section] = [{"type": skill["type"],
                                               "list": filter_string_list(
                        skill["list"], all_keywords)}
                        for skill in data[section]]
                    filtered_data[section] = [
                        skill
                        for skill in filtered_data[section] if skill["list"]]
                    print(f'Filtered {section.capitalize()} Data:',
                          filtered_data[section])
                else:
                    print(
                        f'Unrecognized section: {section}. Data not filtered.')

        print('########### Data filtration complete.')
        return filtered_data

    except Exception as error:
        print('########### Error during data filtration:', str(error))
        return None
