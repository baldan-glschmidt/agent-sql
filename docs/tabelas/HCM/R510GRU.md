# R510GRU

## Descrição

Currículo Web - Grupos de Campos

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| CodPag | Number(003,0) | Não | Código da página do layout |
| CodGru | Number(003,0) | Não | Código do grupo |
| SeqGru | Number(003,0) | Sim | Sequência do grupo |
| NomGru | String(040) | Sim | Nome do grupo |
| TabBas | String(007) | Sim | Tabela-base |
| FilCom | String(2000) | Sim | Filtro - comando SQL aplicado para filtrar os registros da tabela-base |
| PerMin | String(001) | Sim | Permitir minimizar |
| EstIni | Number(001,0) | Sim | Estado inicial - Maximizado ou Minimizado |
| LimReg | Number(002,0) | Sim | Indica o número de registros que podem ser cadastrados pelo currículo |
| Tabela | String(020) | Sim | Nome da tabela de usuário de informações do candidato |

---

## Chave Primária

- CodPer
- IdiLay
- CodPag
- CodGru

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510GRU_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

### IR_R510GRU_002

**Tabela:** R510PAG

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IdiLay | IdiLay |
| CodPag | CodPag |

