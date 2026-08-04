# E063FOT

## Descrição

Tabelas - Cadastros - Fotos.

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdePca | Number(014,0) | Não | Identificador do Processo de Captura das Fotos da Pesagem |
| SeqFot | Number(004,0) | Não | Sequência da Foto |
| CodCam | Number(004,0) | Não | Código da Câmera |
| ImgFot | Image | Sim | Imagem da Foto |
| UrlCam | String(1000) | Não | Endereço URL da Câmera |
| MsgFal | String(255) | Sim | Mensagem de Falha |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- IdePca
- SeqFot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
