
def checkValid(pages, ruleMap):
    for index in range(len(pages)):
        page = pages[index]

        if page in ruleMap:
            mustComeAfter = ruleMap[page]
            appearsBefore = pages[:index]

            for before in appearsBefore:
                if before in mustComeAfter:
                    return False
    return True

# fix with insert sort
def fixIt(pages, ruleMap):
    # Strategy, define a new fixed list, then pop pages off the broken list
    # and insert them before the first page in the fixed list that most come
    # after

    fixed = [pages.pop()]

    # Loop until there are no more pages left to insert
    while not len(pages) == 0:
        page = pages.pop()

        # if any rules for the page to insert
        if page in ruleMap:
            mustComeAfter = ruleMap[page]
            inserted = False

            # loop through the fixed list, finding the first page that must
            # come after out page, and if we find one, insert our page before it
            for index in range(len(fixed)):
                lookingAt = fixed[index]
                if lookingAt in mustComeAfter:
                    fixed.insert(index, page)
                    inserted = True
                    break
        else:
            # no rules for our page, so put it at the end
            fixed.append(page)
            inserted = True

        if not inserted:
            # no pages in the fixed list that must come after this page, so put it at the end
            fixed.append(page)


    return fixed
