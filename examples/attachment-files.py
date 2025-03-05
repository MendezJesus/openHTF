import openhtf as htf

def phase_attachment(test):
    test.attach("test_attachment", "this is test log data.".encode("utf-8"))
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(phase_attachment)
    test.execute(lambda: "PCB001")

if __name__ == "__main__":
    main()
    