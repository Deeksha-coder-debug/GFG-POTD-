class Solution {
    // Function to search a given number in row-column sorted matrix.
    public boolean searchRowMatrix(int[][] mat, int x) {
        // code here
        int st,end,mid;
        for(int i=0;i<mat.length;i++)
        {
            st=0;
            end=mat[i].length-1;
            while(st<=end)
            {
                mid=st+(end-st)/2;
                if(mat[i][mid]==x)
                {
                    return true;
                }
                else if(mat[i][mid]>x)
                {
                    end=mid-1;
                }
                else
                {
                    st=mid+1;
                }
            }
        }
        return false;
    }
}
