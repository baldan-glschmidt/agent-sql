# E000SIS

## Descrição

Tabelas - Integrações - Sistemas Integrados

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| DesInt | String(050) | Não | Descrição do sistema integrado |
| SigInt | String(015) | Não | Sigla do sistema integrado |
| TipInt | Number(002,0) | Não | Tipo de sistema integrado |
| SitReg | String(001) | Não | Situação do registro |
| ExpUnf | String(001) | Sim | Indicativo se o sistema deve exportar apenas uma única foto por produto |
| USU_IntBal | String(001) | Sim | Utiliza Integração Baldan |

---

## Chave Primária

- CodInt

---

## Índices

### E000SISIndice1

**Tipo:** Unico

Campos:
- SigInt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
