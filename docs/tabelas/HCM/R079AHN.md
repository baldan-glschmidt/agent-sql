# R079AHN

## Descrição

Avaliação de Excelência - Notas

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| TipAva | Number(004,0) | Não | Sequência da Avaliação |
| CodHpe | String(004) | Não | Código da Habilidade Pessoal |
| NotAva | Number(005,2) | Sim | Nota da Avaliação da Habilidade |
| MetAva | Number(005,2) | Sim | Meta para a próxima avaliação |
| ComAva | String(3000) | Sim | Comentário |
| BloHpe | String(004) | Sim | Código do Bloco de Habilidades Pessoais |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- TipAva
- CodHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079AHN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R079AHN_005

**Tabela:** R079HPE

| Origem | Destino |
|--------|---------|
| CodHpe | CodHpe |

