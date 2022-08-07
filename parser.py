class Parser:

    def add_char(self, charac):
        self.current_token += charac

    def add_token(self, token_string):
        if token_string == "":
            return
        self.tokens.append(token_string)
        self.current_token = ""

    def __init__(self, code_line):
        self.current_statement_type = 0
        self.current_token = ""
        self.tokens = []
        self.inside_bracket_level = 0

        for character in code_line:
            if self.current_statement_type == 1:
                if character == ")":
                    if self.inside_bracket_level == 0:
                        sub_bracket_tokens = Parser(self.current_token).tokens
                        self.add_token(sub_bracket_tokens)
                        self.current_statement_type = 0
                    else:
                        self.inside_bracket_level -= 1
                        self.add_char(")")
                elif character == "(":
                    self.add_char("(")
                    self.inside_bracket_level += 1
                else:
                    self.add_char(character)

            elif self.current_statement_type == 2:
                if character == '"':
                    self.current_statement_type = 0
                    self.add_token(self.current_token)
                else:
                    self.add_char(character)

            elif character == " " and self.current_token != "":
                self.add_token(self.current_token)

            elif character == "(":
                self.add_token(self.current_token)
                self.inside_bracket_level = 0
                self.current_statement_type = 1

            elif character == '"':
                self.current_statement_type = 2
                self.add_token(self.current_token)
                self.add_token('"')

            else:
                self.add_char(character)

        if self.current_token != "":
            self.tokens.append(self.current_token)