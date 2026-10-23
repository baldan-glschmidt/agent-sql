# R103INS

## Descrição

PSS - Inspeções

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| CodIns | Number(004,0) | Não | Número da Inspeção |
| DatIns | Date | Sim | Data da Inspeção |
| CodIte | Number(004,0) | Sim | Código do Item Avaliado |
| ComIns | String(700) | Sim | Comentários |
| EmpTec | Number(004,0) | Sim | Código empresa do técnico de segurança |
| TipCol | Number(001,0) | Sim | Tipo do Técnico de Segurança |
| NumCad | Number(009,0) | Sim | Cadastro do Técnico de Segurança |
| ComTec | String(700) | Sim | Comentário Técnico |

---

## Chave Primária

- NumEmp
- CodPss
- CodIns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103INS_001

**Tabela:** R103GPS

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPss | CodPss |

### IR_R103INS_004

**Tabela:** R103IAV

| Origem | Destino |
|--------|---------|
| CodIte | CodIte |

