# R110IAT

## Descrição

Atestado/ASO - Anexos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodAte | Number(006,0) | Não | Código do Atendente |
| NumAte | Number(009,0) | Não | Número do Atestado Médico |
| SeqImg | Number(003,0) | Não | Sequência do Anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| DesImg | String(030) | Sim | Descrição do Anexo |
| Imagem | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- CodAte
- NumAte
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110IAT_001

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R110IAT_002

**Tabela:** R110MAM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAte | CodAte |
| NumAte | NumAte |

