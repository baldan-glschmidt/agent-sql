# R058RES

## Descrição

Opções de Resposta para Perguntas da Pesquisa de Satisfação

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Código da pergunta da pesquisa de satisfação |
| CodRes | Number(004,0) | Não | Código da opção de resposta da pergunta de pesquisa de satisfação |
| DesPor | String(030) | Sim | Descrição da opção de resposta em português |
| DesEsp | String(030) | Sim | Descrição da opção de resposta pergunta em espanhol |
| DesIng | String(030) | Sim | Descrição da opção de resposta pergunta em inglês |

---

## Chave Primária

- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058RES_000

**Tabela:** R058PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

