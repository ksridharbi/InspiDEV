CREATE FUNCTION dbo.NumberToWords (@Number INT)
RETURNS VARCHAR(255)
AS
BEGIN
    DECLARE @Words VARCHAR(255);

    -- This is just a demo. Extend as needed.
    IF @Number = 1 SET @Words = 'One';
    ELSE IF @Number = 2 SET @Words = 'Two';
    ELSE IF @Number = 3 SET @Words = 'Three';
    ELSE IF @Number = 4 SET @Words = 'Four';
    ELSE IF @Number = 5 SET @Words = 'Five';
    ELSE SET @Words = CAST(@Number AS VARCHAR); -- fallback to digits

    RETURN @Words;
END;