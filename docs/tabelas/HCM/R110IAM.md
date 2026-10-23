# R110IAM

## Descrição

Atendimentos - Anexos

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodFic | Number(009,0) | Não | Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| SeqImg | Number(003,0) | Não | Sequência da Imagem |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| DesImg | String(030) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Anexo |
| SitAss | Number(001,0) | Sim | Status da assinatura digital do documento |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110IAM_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110IAM_003

**Tabela:** R110MAT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |
| DatAte | DatAte |
| HorAte | HorAte |

