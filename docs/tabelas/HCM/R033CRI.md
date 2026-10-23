# R033CRI

## Descrição

Pessoas - Critérios de comparação da geração de pessoas

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| OriCri | Number(001,0) | Não | Origem do critério de comparação |
| CodReg | Number(002,0) | Não | Código da regra de comparação |
| SeqCri | Number(004,0) | Não | Sequência do critério de comparação |
| Tabel1 | String(020) | Sim | Tabela do Campo 1 |
| Campo1 | String(020) | Sim | Campo 1 |
| Campo2 | String(020) | Sim | Campo 2 |
| CasSen | String(001) | Sim | Case Sensitive |
| AceTex | String(001) | Sim | Acentuação |
| DifZer | String(001) | Sim | Compara <> 0 |

---

## Chave Primária

- OriCri
- CodReg
- SeqCri

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033CRI_001

**Tabela:** R033REG

| Origem | Destino |
|--------|---------|
| OriCri | OriCri |
| CodReg | CodReg |

