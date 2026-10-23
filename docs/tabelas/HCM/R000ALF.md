# R000ALF

## Descrição

Lista das tabelas/campos convertidos para o cnpj alfanumérico

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomTab | String(010) | Não | Nome tabela que será convertida no cnpj alfanumérico |
| CamOld | String(010) | Não | Nome do Campo antigo que será convertido para o cnpj alfanumérico |
| CamNew | String(010) | Não | Nome do Campo novo que receberá o cnpj alfanumérico |
| QtdUpd | Number(006,0) | Sim | Quantidade de linhas por Update |
| MsgCnv | String(500) | Sim | Mensagem conversão da última execução |
| CamTip | String(010) | Sim | Campo que determina o tipo do conteúdo cnpj/cei/cpf/outros |
| LstTip | String(500) | Sim | Lista de tipos e quantidades de caracteres a serem completados |
| ExeCnv | Number(001,0) | Sim | Status da conversão - 0-Nunca atualizado/1-Atualizado, não indica finalizado |
| TipCnv | Number(001,0) | Sim | Tipo conversão - 0-Total/1-Parcial |
| UltDat | Date | Sim | Data da última execução, para uso na próxima execução |

---

## Chave Primária

- NomTab
- CamOld

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
