# E056COR

## Descrição

Cadastros - Tributos - Corretores

---

## Resumo

- Campos: 20
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCor | Number(009,0) | Não | Código do corretor |
| NomCor | String(060) | Não | Nome do corretor |
| ApeCor | String(060) | Sim | Nome fantasia do corretor |
| TipCor | String(001) | Sim | Tipo do documento do corretor |
| DocIdeCor | String(014) | Sim | Número do CNPJ ou CPF do corretor |
| EndCor | String(100) | Sim | Endereço do corretor |
| CplEnd | String(200) | Sim | Complemento do endereço do corretor (sala, andar, etc.) |
| ZipCor | String(014) | Sim | Código da cidade do corretor externo - ZIP CODE |
| CepCor | Number(008,0) | Sim | CEP do endereço do corretor |
| BaiCor | String(075) | Sim | Bairro do corretor |
| CidCor | String(060) | Sim | Cidade do corretor |
| SigUfs | String(002) | Sim | Estado do corretor |
| FonCor | String(020) | Sim | Número do telefone - 1 |
| FonCo2 | String(020) | Sim | Número do telefone - 2 |
| FonCo3 | String(020) | Sim | Número do telefone - 3 |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| DatCad | Date | Sim | Data do cadastramento do corretor |
| DatAtu | Date | Sim | Data da última alteração do corretor |
| SitCor | String(001) | Não | Situação do corretor |

---

## Chave Primária

- CodEmp
- CodCor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
