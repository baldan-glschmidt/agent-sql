# R059USU

## Descrição

Cadastro de Leitoras do Usuário

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodUsu | Number(010,0) | Não | Código do Grupo/Usuário do Processamento |
| CodLei | Number(003,0) | Não | Código da Leitora |
| PorCom | Number(001,0) | Sim | Porta Serial de Comunicação |
| DirCfg | String(255) | Sim | Diretório do Arquivo de Criptografia (cliente.cfg) |
| StaLei | Number(001,0) | Sim | Status da Leitora |
| UtlLea | String(001) | Sim | Utiliza leitura automática |
| CodMsc | Number(002,0) | Sim | Código Mapa Smart Card |

---

## Chave Primária

- CodUsu
- CodLei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R059USU_001

**Tabela:** R059LEI

| Origem | Destino |
|--------|---------|
| CodLei | CodLei |

