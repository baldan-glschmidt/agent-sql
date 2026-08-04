# E077FAV

## Descrição

Cadastros - Favorecidos

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFav | Number(014,0) | Sim | Número do CNPJ ou CPF do favorecido |
| DocIdeFav | String(014) | Sim | Número do CNPJ ou CPF do favorecido |
| TipFav | String(001) | Não | Tipo favorecido |
| NomFav | String(100) | Não | Nome do favorecido |
| ApeFav | String(050) | Sim | Nome fantasia do favorecido |
| EndFav | String(035) | Sim | Endereço do favorecido |
| NumEnd | Number(005,0) | Sim | Número do Endereço do Sacado |
| CplEnd | String(200) | Sim | Complemento do endereço do favorecido (sala, andar, etc.) |
| CepFav | Number(008,0) | Sim | CEP do favorecido |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade do favorecido |
| BaiFav | String(075) | Sim | Bairro do favorecido |
| CidFav | String(060) | Sim | Cidade do favorecido |
| SigUfs | String(002) | Sim | Sigla do estado do favorecido |
| FonFav | String(020) | Sim | Número do telefone do favorecido |
| FaxFav | String(020) | Sim | Número do FAX do favorecido |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do favorecido |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| CodBan | String(003) | Sim | Código do banco da conta corrente do favorecido |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente do favorecido |
| CcbFav | String(014) | Sim | Número da conta corrente do favorecido no banco |
| DatCad | Date | Sim | Data do cadastramento do favorecido |
| DatAtu | Date | Sim | Data da última alteração do cadastro do favorecido |
| SitFav | String(001) | Não | Situação do favorecido |
| EenFav | String(018) | Sim | Código do endereço do favorecido |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| USU_IdeFav | String(040) | Sim | Alguns Favorecidos informa o codigo de identificacao para o pagto.ou deposito |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
