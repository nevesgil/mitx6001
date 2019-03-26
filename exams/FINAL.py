####################################################################################################
def uniqueValues(aDict):
    return sorted([k for k in aDict if all(aDict[k] != aDict[o] for o in aDict if o != k)])
	
	
	
#######################################################################################################
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    elif len(L1) != len(L2):
        return False
    else:
        lst = L1[:]
        for element in L1:
            if element in L2:
                L2.remove(element)
        if len(L2) == 0:
            res_dict = {}
            for item in lst:
                res_dict[item] = res_dict.get(item, 0) + 1
                most = max(res_dict.values())
                for k, v in res_dict.items():
                    if v == most:
                        most_elmt = k
            return (most_elmt, most, type(most_elmt))
        else:
            return False
			
			
#######################################################################################################

# this code is not 100% 

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        self.name = name
        self.status = status
        
        
    def getStatus(self):
        """
        Returns the status
        """
        if self.status not in ['citizen', 'legal_resident', 'illegal_resident']:
            raise ValueError
        return self.status
    
    
    
    
    
################################################################################################## 
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals:
            del self.vals[e]


    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise.
           """
        if e in self.vals:
            return True
        else:
            return False
        




