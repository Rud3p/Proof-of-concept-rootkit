```mermaid
graph TD;
    A[Import Libraries]-->B[Load ntdll.dll];
    B-->C[Get System Call Addresses];
    C-->D[Save Original Calls];
    D-->E[Define Detours];
    E-->F[Overwrite System Calls];
    F-->G[Print "Installed!"];
    G-->H[Open and Close Test File];
    H-->I[Redirect Output to Log];
    I-->J{Messages in Log?};
    J--Yes-->K[Print "Works!"];
    J--No-->L[Print "Failed"];
    L-->M[Create Registry Key];
    M-->N[Print "Persisted!"];
```
