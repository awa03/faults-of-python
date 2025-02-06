#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void* task(void* arg) {
    char* name = (char*)arg;
    pid_t pid = getpid();
    pthread_t tid = pthread_self();

    for (int i = 0; i < 100; i++) {
        printf("Child: Task %s, iteration %d, PID %d, Thread ID %lu\n",
               name, i, pid, (unsigned long)tid);
        sleep(1);
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    char *name1 = "A";
    char *name2 = "B";

    printf("Parent: PID %d\n", getpid());

    // run in parallel (or concurrently depending on machine resources)
    pthread_create(&thread1, NULL, task, name1);
    pthread_create(&thread2, NULL, task, name2);

    // join thread to main thread
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    sleep(100);

    printf("All threads completed\n");
    return 0;
}
