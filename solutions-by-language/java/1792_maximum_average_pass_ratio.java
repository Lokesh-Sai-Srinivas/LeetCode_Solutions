import java.util.PriorityQueue;

class Solution {
    static class ClassRatio {
        int pass;
        int total;

        ClassRatio(int p , int t) {
            this.pass = p;
            this.total = t;
        }

        void addStudent() {
            pass++;
            total++;
        }

        double ratio () {
            return (double) pass/ total;
        }

        double gain() {
            return ((double) (pass + 1) / (total + 1)) - ratio();
        }
    }
    
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<ClassRatio> maxHeap = new PriorityQueue<> ((a,b) -> Double.compare(b.gain(), a.gain()));
        
        for (int [] cls :classes) {
            maxHeap.offer(new ClassRatio(cls[0], cls[1]));
        }

        for(int i = 0 ; i < extraStudents; i++){
            ClassRatio best = maxHeap.poll();
            best.addStudent();
            maxHeap.offer(best);
        }

        double total = 0.0;
        for(ClassRatio cls: maxHeap) {
            total += cls.ratio();
        }
        return total / classes.length;
    }

}