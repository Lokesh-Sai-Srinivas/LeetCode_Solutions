"""
Problem: 1792 - Maximum Average Pass Ratio  
Description: You are given a list of classes, each represented by [pass_i, total_i], and an integer extraStudents. Each extra student is guaranteed to pass any class they are assigned to. Assign these students to classes to maximize the average pass ratio across all classes. The pass ratio of a class is pass_i / total_i. Return the maximum possible average pass ratio after assigning all extra students.  
Date: 2025-09-01
"""

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
