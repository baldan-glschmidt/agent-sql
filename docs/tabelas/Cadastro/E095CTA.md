# E095CTA

## Descrição

Cadastros - Fornecedores - Assunto X Contato

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodAss | String(003) | Não | Código do assunto |
| SeqCto | Number(005,0) | Não | Pessoa de contato |
| ObsCto | String(030) | Sim | Observações |

---

## Chave Primária

- CodFor
- CodAss
- SeqCto

---

## Índices

### E095CTAIndice1

**Tipo:** Não unico

Campos:
- CodAss

### E095CTAIndice2

**Tipo:** Não unico

Campos:
- CodFor
- SeqCto

---

## Relacionamentos

### IR_E095CTA_001

**Tabela:** E060TAS

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |

### IR_E095CTA_002

**Tabela:** E095CTO

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |
| SeqCto | SeqCto |

