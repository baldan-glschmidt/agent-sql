# E000ERA

## Descrição

Cadastros - Processos Automáticos - Entrada de Relatórios

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPra | Number(004,0) | Não | Código do processo automático |
| NomVar | String(045) | Não | Nome da variável do modelo de relatório |
| ValNum | Number(018,4) | Sim | Valor numérico para a variável do modelo de relatório |
| ValStr | String(3960) | Sim | Valor alfanumérico para a variável do modelo de relatório |

---

## Chave Primária

- CodPra
- NomVar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E000ERA_000

**Tabela:** E000AGE

| Origem | Destino |
|--------|---------|
| CodPra | CodPra |

