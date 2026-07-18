#include <stdio.h>
#include <stdlib.h>

#define MAX_FRAMES 50

int main() {
    int totalFrames, windowSize;
    printf("Enter total number of frames to send: ");
    scanf("%d", &totalFrames);
    printf("Enter window size: ");
    scanf("%d", &windowSize);

    int sentUpto = 0;
    srand(0);  // fixed seed for predictable behavior

    while (sentUpto < totalFrames) {
        int windowEnd = sentUpto + windowSize;
        if (windowEnd > totalFrames) windowEnd = totalFrames;

        printf("\nSending frames: ");
        for (int i = sentUpto; i < windowEnd; i++)
            printf("[%d] ", i);

        // Simulate whether ACK is lost or not
        int ackLoss = rand() % 2;  // 0 = no loss, 1 = loss

        if (ackLoss) {
            int ackFrame = sentUpto + rand() % (windowEnd - sentUpto);
            printf("\nACK lost for Frame %d. Go-Back-N triggered.", ackFrame);
            printf("\nResending from Frame %d...\n", ackFrame);
            sentUpto = ackFrame;  // Go back to that frame
        } else {
            printf("\nAll ACKs received for current window.");
            printf("\nSliding window forward.\n");
            sentUpto = windowEnd;  // Move to next window
        }
    }

    printf("\nAll frames sent successfully with Go-Back-N.\n");
    return 0;
}
