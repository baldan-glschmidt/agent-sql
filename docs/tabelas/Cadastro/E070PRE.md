# E070PRE

## Descrição

Cadastros - Mercado e Suprimentos - Parâmetros do Recebimento Eletrônico

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| GerMde | String(001) | Sim | Gerar Manifestação do Destinatário |
| PrzMde | Number(003,0) | Sim | Prazo para geração da Manifestação do Destinatário (dias) |
| RetMde | String(001) | Sim | Tipo de Retorno da Manifestação do Destinatário |
| DirMde | String(250) | Sim | Diretório de Geração da Manifestação do Destinatário |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Não | Usuário responsável pela última alteração do registro |
| PrvNfc | Number(004,0) | Sim | Identificador do provedor de serviços |
| SrvNfc | Number(004,0) | Sim | Identificador do serviço |
| PrtNfc | Number(004,0) | Sim | Identificador sequencial da porta |
| PrmNfc | Number(002,0) | Sim | Sequencial de quebra dos parâmetros |
| LogNfc | String(050) | Sim | Usuário para autenticação com o sistema de Documentos Eletrônicos para NFC-e |
| SenNfc | String(100) | Sim | Senha para autenticação com o sistema de Documentos Eletrônicos para NFC-e |
| SugOcp | String(001) | Sim | Sugerir Ordem de Compra no Recebimento Eletrônico |

---

## Chave Primária

- IdeUni

---

## Índices

### E070PREIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
