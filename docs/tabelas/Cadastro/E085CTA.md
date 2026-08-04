# E085CTA

## Descrição

Cadastros - Clientes - Assuntos X Contatos

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
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodAss | String(003) | Não | Código do assunto |
| SeqCto | Number(005,0) | Não | Pessoa de contato |
| ObsCto | String(255) | Sim | Observações |

---

## Chave Primária

- CodCli
- CodAss
- SeqCto

---

## Índices

### E085CTAIndice1

**Tipo:** Não unico

Campos:
- CodAss

### E085CTAIndice2

**Tipo:** Não unico

Campos:
- CodCli
- SeqCto

---

## Relacionamentos

### IR_E085CTA_001

**Tabela:** E060TAS

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |

### IR_E085CTA_002

**Tabela:** E085CTO

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |
| SeqCto | SeqCto |

