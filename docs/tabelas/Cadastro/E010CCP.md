# E010CCP

## Descrição

Cadastros - Características de Produto - Componentes

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodCte | String(003) | Não | Código da característica de produto |
| SeqCcp | Number(009,0) | Não | Sequência do componente da característica de produto |
| DesCcp | String(250) | Não | Componente da característica de produto |
| ObsCcp | String(240) | Sim | Observação do componente da característica de produto |

---

## Chave Primária

- CodEmp
- CodCte
- SeqCcp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E010CCP_001

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

