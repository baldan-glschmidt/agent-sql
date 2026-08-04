# E042CPD

## Descrição

Tabelas - Contas Contábeis Padrões

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCpd | Number(004,0) | Não | Código numérico de identificação da conta contábil padrão |
| DesCpd | String(020) | Não | Descrição do código de identificação da conta contábil padrão |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |

---

## Chave Primária

- CodEmp
- CodCpd

---

## Índices

### E042CPDIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CtaRed

---

## Relacionamentos

### IR_E042CPD_003

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaRed | CtaRed |

