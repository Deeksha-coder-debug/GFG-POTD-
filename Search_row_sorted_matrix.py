#Function to search a given number in row-column sorted matrix.
def searchRowMatrix(self, mat, x): 
        # code here 
        for row in mat:
            st=0
            end=len(mat[0])-1
            while st<=end:
                mid=st+(end-st)//2
                if row[mid]==x:
                    return True
                elif row[mid]>x:
                    end=mid-1
                else:
                    st=mid+1
        return False
