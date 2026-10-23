# R078DEF

## Descrição

Definições de Política Salarial

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DesPol | String(2000) | Sim | Descrição da Política Salarial |
| TmpAvl | Number(002,0) | Sim | Tempo em Meses que faz as Avaliações. |
| CodReg | Number(003,0) | Sim | Código da Regra a ser Executada na Gravação de Proposta Salarial ou de Cargo |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R078DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

