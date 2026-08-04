# E000ODW

## Descrição

Tabelas - Integrações - Ordens de separação/recebimento

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumOrd | String(020) | Não | Número da ordem de separação/recebimento |
| TipOrd | Number(001,0) | Não | Tipo da ordem de separação/recebimento |
| SitOrd | Number(001,0) | Não | Situação da ordem de separação/recebimento |
| IndPro | String(001) | Sim | Proc. Faturamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| OrdOri | String(020) | Sim | Número da ordem de separação que está sendo cancelada |
| PrdOrd | Number(001,0) | Sim | Procedência da ordem de separação/recebimento |

---

## Chave Primária

- CodEmp
- CodFil
- NumOrd

---

## Índices

### E000ODWIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- IndPro

### E000ODWIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- TipOrd
- SitOrd

---

## Relacionamentos

Nenhum relacionamento cadastrado.
