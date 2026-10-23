# R577REV

## Descrição

Competência - Revisão

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCpt | Number(009,0) | Não | Código da Competência |
| RevCpt | String(010) | Não | Código da revisão da Competência |
| DesRev | String(060) | Sim | Descrição da revisão da Competência |
| DatIni | Date | Sim | Data de início de validade da revisão da competência |
| DatTer | Date | Sim | Data de término da revisão da competência |
| ValRev | Number(003,0) | Sim | Informe por quantos meses o registro da competência é válido para uma pessoa |
| CodTpr | Number(004,0) | Sim | Indica a Tabela de proficiências válida para a revisão da competência |
| InfPAp | String(001) | Sim | Indica se o Perfil deve ou não ser informado quando se registra a competência |
| DesDet | String(2000) | Sim | Descrição detalhada da competência |
| EqvAnt | String(001) | Sim | Indica que a revisão é equivalente à anterior |

---

## Chave Primária

- CodCpt
- RevCpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577REV_000

**Tabela:** R577CPT

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |

### IR_R577REV_006

**Tabela:** R577PRO

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |

