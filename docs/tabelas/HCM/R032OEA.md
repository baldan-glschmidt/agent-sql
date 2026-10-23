# R032OEA

## Descrição

Outras Empresas - Seguridade

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| CodSeg | Number(004,0) | Não | Código de Seguridade |
| PerSeg | Number(007,4) | Sim | % Seguridade |

---

## Chave Primária

- CodOem
- CodSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032OEA_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R032OEA_001

**Tabela:** R026SEG

| Origem | Destino |
|--------|---------|
| CodSeg | CodSeg |

