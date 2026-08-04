# E062RET

## Descrição

Tabelas - Localidades de Retirada

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRet | Number(004,0) | Não | Código do local de retirada. |
| TipRet | String(001) | Não | Tipo de local de retirada. |
| CgcRet | Number(014,0) | Sim | Número do CNPJ/CPF de retirada. |
| DocIdeRet | String(014) | Sim | Número do CNPJ/CPF de retirada. |
| EndRet | String(100) | Não | Endereço de retirada. |
| NenRet | String(060) | Não | Número do endereço de retirada. |
| CplRet | String(150) | Sim | Complemento do endereço de retirada. |
| BaiRet | String(075) | Não | Bairro do local retirada. |
| CidRet | String(060) | Não | Cidade do endereço de retirada. |
| EstRet | String(002) | Não | Estado do endereço de retirada. |
| CepRet | Number(008,0) | Não | CEP do endereço de retirada. |
| IniRet | Number(008,0) | Não | Faixa inicial do CEP do endereço de retirada. |
| DatAlt | Date | Sim | Data da última alteração do registro. |
| HorAlt | Number(005,0) | Sim | Hora/minuto da última alteração do registro. |
| UsuAlt | Number(010,0) | Não | Usuário responsável pela última alteração |
| SitReg | String(001) | Não | Situação do registro |
| NomRet | String(060) | Sim | Razão social do endereço de retirada |
| FonRet | String(020) | Sim | Telefone do endereço de retirada |
| EmaRet | String(060) | Sim | E-mail do endereço de retirada |
| InsRet | String(025) | Sim | Inscrição estadual do endereço de retirada |

---

## Chave Primária

- CodRet

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
