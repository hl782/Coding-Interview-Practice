public class eopi_ch6 {
  public static void main(String[] args){
    int[] arr = new int[]{3, 1, 5, 4, -1, 2, 6, 0, 4};
    int[] sol = dutchNationalFlag(arr, 3);
    for(int x = 0; x < sol.length; x++){
      System.out.print(sol[x] + " ");
    }
  }


  public static int[] dutchNationalFlag(int[] arr, int index){
    // My solution of 2 passes for grouping elements < pivot, and elements > pivot

    // int pivot = arr[index];
    // int left = 0;
    // int right = arr.length-1;
    //
    // for(int x = 0; x < arr.length; x++){
    //   if (arr[x] < pivot){
    //     int temp = arr[x];
    //     arr[x] = arr[left];
    //     arr[left] = temp;
    //     left++;
    //   }
    // }
    //
    // for(int x = arr.length-1; x > 0; x--){
    //   if (arr[x] > pivot){
    //     int temp = arr[x];
    //     arr[x] = arr[right];
    //     arr[right] = temp;
    //     right--;
    //   }
    // }
    //
    // return arr;

    //The efficient solution in 1 pass - O(n)
    int pivot = arr[index];
    int left = 0;
    int middle = 0;
    int right = arr.length-1;

    while(middle <= right){
      if (arr[middle] < pivot){
        int temp = arr[left];
        arr[left] = arr[middle];
        arr[middle] = temp;
        left++;
        middle++;
      } else if (arr[middle] > pivot){
        int temp = arr[right];
        arr[right] = arr[middle];
        arr[middle] = temp;
        right--;
      } else {
        middle++;
      }
    }
    return arr;
  }

  public static int[] arbitraryPrecisionNumber(int [] arr){
    return [];
  }
}
