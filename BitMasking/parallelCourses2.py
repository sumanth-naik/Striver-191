


# TLE
from copy import deepcopy
class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        # 1 indexing
        indegreeArr, adjList = [0 for _ in range(n+1)], [[] for _ in range(n+1)]
        for prevCourse, nextCourse in relations:
            indegreeArr[nextCourse] += 1
            adjList[prevCourse].append(nextCourse)
        
        possibleCoursesForThisSemArr = [i for i in range(1, n+1) if indegreeArr[i]==0]
        memo = {}
        def getCombinations(combinationSoFar, possibleCoursesForThisSemArr, index, allCombinations):         
            if len(possibleCoursesForThisSemArr)<=k and index==0:
                allCombinations.append(set(possibleCoursesForThisSemArr))
                return
            if len(combinationSoFar)==k:
                allCombinations.append(combinationSoFar)
                return
            if len(combinationSoFar)>k or index==len(possibleCoursesForThisSemArr):
                return
            
            getCombinations(combinationSoFar, possibleCoursesForThisSemArr, index+1, allCombinations)
            getCombinations(combinationSoFar.union([possibleCoursesForThisSemArr[index]]), possibleCoursesForThisSemArr, index+1, allCombinations)


        def kahnsTopoSort(possibleCoursesForThisSemArr, indegreeArr):
            if len(possibleCoursesForThisSemArr)==0:
                return 0
            if (tuple(sorted(possibleCoursesForThisSemArr)), tuple(indegreeArr)) in memo:
                return memo[(tuple(sorted(possibleCoursesForThisSemArr)), tuple(indegreeArr))]
            minNumSems = 1e9
            allCombinations = []
            getCombinations(set(), possibleCoursesForThisSemArr, 0, allCombinations)
            for combination in allCombinations:
                possibleCoursesForNextSemArr = []
                indegreeArrForNextSem = deepcopy(indegreeArr)
                for course in possibleCoursesForThisSemArr:
                    if course in combination:
                        for nextCourse in adjList[course]:
                            indegreeArrForNextSem[nextCourse] -= 1
                            if indegreeArrForNextSem[nextCourse]==0:
                                possibleCoursesForNextSemArr.append(nextCourse)
                    else:
                        possibleCoursesForNextSemArr.append(course)

                minNumSems = min(minNumSems, kahnsTopoSort(possibleCoursesForNextSemArr, indegreeArrForNextSem) + 1)     
            memo[(tuple(sorted(possibleCoursesForThisSemArr)), tuple(indegreeArr))] = minNumSems               
            return minNumSems

        return kahnsTopoSort(possibleCoursesForThisSemArr, indegreeArr)




# bitmasking DP with nChooseK generation
class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        # (1<<i) -> left shift i times ~ pow(2,i)
        # ith bit set in index indicates that course has been completed
        # index 3 -> 101 in binary means a state where courses 0 and 2 are taken
        # last index means all courses are taken which will have the final answer  
        dpArrOfCourseMasks = [n for _ in range(1<<n)]
        # doing no courses takes 0 sems
        dpArrOfCourseMasks[0] = 0

        # used for cleverly taking courses which can unlock others
        outdegreeArr = [0 for _ in range(n)]

        # stores bitmask rep of required courses for each course
        # if course 0 requires course 1 and 3, 0th index of arr has 1010
        arrOfPreReqCoursesStoredAsMasks = [0 for _ in range(n)]
        for prevCourse, nextCourse in relations:
            # relations is 1 indexed
            # taking an or for a number is similar to appending to adjList
            arrOfPreReqCoursesStoredAsMasks[nextCourse-1] |= 1<<(prevCourse-1)
            outdegreeArr[prevCourse-1] += 1

        def getCombinationOfSize(coursesThatCanBeTakenUp, sizeOfFinalCombination, allCombinations, courseCombination = [], index = 0):
            if len(courseCombination)==sizeOfFinalCombination:
                allCombinations.append(courseCombination)
                return 
            if len(courseCombination)>sizeOfFinalCombination or index==len(coursesThatCanBeTakenUp):
                return
            
            getCombinationOfSize(coursesThatCanBeTakenUp, sizeOfFinalCombination, allCombinations, courseCombination, index+1)
            getCombinationOfSize(coursesThatCanBeTakenUp, sizeOfFinalCombination, allCombinations, courseCombination+[coursesThatCanBeTakenUp[index]], index+1)


        # fill DP
        for coursesMask in range(1<<n):
            coursesThatCanBeTakenUp = []
            for course in range(n):
                #   if it has not been done         and  all the pre reqs are complete
                if (coursesMask & (1<<course) == 0) and (arrOfPreReqCoursesStoredAsMasks[course] & coursesMask == arrOfPreReqCoursesStoredAsMasks[course]):
                    coursesThatCanBeTakenUp.append(course)

            coursesThatCanUnlockOthers = [course for course in coursesThatCanBeTakenUp if outdegreeArr[course]>0]
            coursesThatCanNotUnlockOthers = [course for course in coursesThatCanBeTakenUp if outdegreeArr[course]==0]
            
            if len(coursesThatCanUnlockOthers)<=k:
                coursesMaskAfterTakingTheCoursesThatAreChosen = coursesMask
                for chosenCourse in coursesThatCanUnlockOthers + coursesThatCanNotUnlockOthers[:k-len(coursesThatCanUnlockOthers)]:
                    coursesMaskAfterTakingTheCoursesThatAreChosen |= (1<<chosenCourse)

                # from this state of courses, if we take the chosenCourses and find it takes less semesters than previously seen, then update
                dpArrOfCourseMasks[coursesMaskAfterTakingTheCoursesThatAreChosen] = min(dpArrOfCourseMasks[coursesMaskAfterTakingTheCoursesThatAreChosen], 
                                                                                        dpArrOfCourseMasks[coursesMask]+1)

            else:
                allCombinations = []
                getCombinationOfSize(coursesThatCanUnlockOthers, min(k, len(coursesThatCanUnlockOthers)), allCombinations)

                for coursesThatAreChosen in allCombinations:
                    coursesMaskAfterTakingTheCoursesThatAreChosen = coursesMask
                    for chosenCourse in coursesThatAreChosen:
                        coursesMaskAfterTakingTheCoursesThatAreChosen |= (1<<chosenCourse)

                    # from this state of courses, if we take the chosenCourses and find it takes less semesters than previously seen, then update
                    dpArrOfCourseMasks[coursesMaskAfterTakingTheCoursesThatAreChosen] = min(dpArrOfCourseMasks[coursesMaskAfterTakingTheCoursesThatAreChosen], 
                                                                                            dpArrOfCourseMasks[coursesMask]+1)

        return dpArrOfCourseMasks[-1]